function [vasculature] = segment_CoW (currFileData,toDisplay) 

%% Parse input
% Data can be the filename, the actual NIFTY data 
if isa(currFileData,'char')
    currFileDataName = currFileData;
    currFileData=niftiread(currFileDataName);   
end

if ~exist('currFileDataName','var')
    currFileDataName = ' ';
end
if ~exist('toDisplay','var')
    toDisplay = 0;
end



[rows,cols,levs]                = size(currFileData);
%% Normalise and crop
currFileROI                     = double(currFileData)/max(double(currFileData(:)));
currFileROI([1:85 485:end],:,:) = 0;
currFileROI(:,[1:70 495:end],:) = 0;
maxIntensProj                   = (squeeze(max(currFileROI,[],3)));

%% Iterative region growing

se                              = strel('sphere',3);
seedRegions                     = currFileROI>0.65;
seedRegionsDil                  = imdilate(seedRegions,se);
%%
for k=0.55:-0.1:0.1
    %clf
    %surfdat(seedRegions,'ko')
    %k=0.15;
    [currentROIs,numROIs]       = bwlabeln((currFileROI>k).*(currFileROI<=(k+0.1)));
    currentROIS_P1               = regionprops(currentROIs,'Area');
    %currentROIS_P2               = regionprops3(currentROIs,'PrincipalAxisLength');
    % only keep overlapping 
    regionsToKeep1               = unique(currentROIs.*seedRegionsDil);
    regionsToKeep2               = regionsToKeep1(2:end);
    if (k<0.45)&(k>=0.25)
        regionsToKeep3              = find([currentROIS_P1.Area]<100000);
        regionsToKeep4              = intersect(regionsToKeep2,regionsToKeep3);       
    elseif k<0.25
        regionsToKeep3              = find([currentROIS_P1.Area]<1000);
        regionsToKeep4              = intersect(regionsToKeep2,regionsToKeep3);
    else
        regionsToKeep4          = regionsToKeep2;
    end
    %regionsToKeep() = [];
    %currentROIS_P12              = currentROIS_P1(regionsToKeep);
    %currentROIS_P22              = currentROIS_P2(regionsToKeep(2:end,'PrincipalAxisLength'));
    keepROIs                    = ismember(currentROIs,regionsToKeep4);
    seedRegions                 = seedRegions|keepROIs; 
    seedRegionsDil              = imdilate(seedRegions,se);
    % surfdat(keepROIs,'r.')
end
vasculature0(rows,cols,levs)     = 0;
for k=1:levs
    %vasculature(:,:,k)       = imclose(vasculature(:,:,k),[0 1 0;1 1 1; 0 1 0]);
    vasculature0(:,:,k)       = imclose(seedRegions(:,:,k),strel('disk',2));
    vasculature0(:,:,k)       = imfill(vasculature0(:,:,k),'holes');

end
%vasculature2                = bwmorph3(vasculature,'clean');

vasculature_L               = bwlabeln(vasculature0);
vasculature_P               = regionprops3(vasculature_L,'Volume');
vasculature2                = ismember(vasculature_L,find([vasculature_P.Volume]>10));
[vasculature3,numReg]       = bwlabeln(vasculature2);
vasculatureSk               = bwskel(vasculature2>0);
vasculature_branchP         = bwmorph3(vasculatureSk,'branchpoints');
%branchpoints are no single points, reduce by looking at the points that
%have more than one voxel
vasculature_branchP_L= bwlabeln(vasculature_branchP);
bP_L_pos   = find(vasculature_branchP_L(:));
bP_labels   = vasculature_branchP_L(bP_L_pos);
bP_unique   = unique(vasculature_branchP_L(bP_L_pos));
bP_count    = accumarray(vasculature_branchP_L(bP_L_pos),1);
bP_repeated = find(bP_count>1);

for counter_bp=1:numel(bP_repeated)
    curr_bP = find(bP_labels==bP_repeated(counter_bp));
    vasculature_branchP(bP_L_pos (curr_bP(2:end)))=0;
end

% save all parameters in a struct
vasculature.vessels         = vasculature2;
vasculature.vesselsL        = vasculature3;
vasculature.skeleton        = vasculatureSk;
vasculature.branchPoints    = vasculature_branchP;
vasculature.maxIntensity    = maxIntensProj;
vasculature.numBranchPoints = sum(vasculature.branchPoints(:));
vasculature.name            = currFileDataName;
vasculature.vesselLength    = sum(vasculature.skeleton(:));
vasculature.rawData         = currFileData;
vasculature.numSlices       = levs;
% Analyse if the three main elements in the base are connected or not
%%
baseVasculature1            = max(vasculature.vesselsL(:,:,1:20),[],3);
baseVasculature2            = max(vasculature.vesselsL(:,:,1:60),[],3);
baseProps1                   = regionprops(baseVasculature1,'area','boundingbox','centroid');
baseProps2                   = regionprops(baseVasculature2,'area','boundingbox','centroid');
%% Display options for an app
dataDouble                  = double(currFileData);
maxIntensityRaw             = max(dataDouble(:));
vasculature.rows            = rows;
vasculature.cols            = cols;

sagD                        = permute(uint8(255*dataDouble/maxIntensityRaw),[3 1 2]);
corD                        = permute(uint8(255*dataDouble/maxIntensityRaw),[3 2 1]);
vasculature.maxIntensity2   = uint8(255*max(dataDouble,[],3)/maxIntensityRaw);
vasculature.maxIntensityS   = max(sagD(end:-1:1,:,:),[],3);
vasculature.maxIntensityC   = max(corD(end:-1:1,:,:),[],3);
vasculature.scaledData      = uint8(255*vasculature.rawData/(0.9*maxIntensityRaw));
vasculature
    

%%
if numel(baseProps2) ==1
    % Single case, all sides are connected
else
    % two or more, most likely 2 or 3, discard small specs
    [topAreas,topRegions] = sort([baseProps2.Area],'descend');
    topAreasPercent         = topAreas/topAreas(1);
    mainRegions             = topRegions(topAreasPercent>0.05);
    numRegions              = numel(mainRegions);
end

vasculature.mainRegions     = mainRegions;
vasculature.numRegions      = numRegions;
vasculature.totRegions      = numReg;

%%

if toDisplay ==1
    display_CircleOfWillis(vasculature)
%     h1=figure;
%     h1.Position = [270    370    1017   384];
%     subplot(121)
%     imagesc(vasculature.maxIntensity);colorbar
%     if exist('currFileDataName','var')
%         title(currFileDataName,'interpreter','none')
%     end
%     colormap bone
%     subplot(122)
%     [f,v]=isosurface(vasculature.vessels,0.05);
%     [f2,v2]=isosurface(vasculature.skeleton,0.05);
%     
%     se = strel('sphere',3);
% 
%     [f3,v3]=isosurface(imdilate(vasculature.branchPoints,se),0.05);
%     
%     hPatch = patch('Faces',f,'Vertices',v,'edgecolor','none','facecolor','r');
%     hPatch2 = patch('Faces',f2,'Vertices',v2,'edgecolor','none','facecolor','b');
%     hPatch3 = patch('Faces',f3,'Vertices',v3,'edgecolor','none','facecolor','g');
%     
%     lighting phong
%     camlight left
%     view(128,6)
%     camlight right   
%     axis tight
%     hPatch.FaceAlpha = 0.2;
end