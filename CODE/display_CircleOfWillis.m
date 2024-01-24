function handleFig = display_CircleOfWillis(vasculature)


    handleFig=figure;
    handleFig.Position = [270    370    1017   384];
    handleFig.UserData = vasculature.rawData;

    h131=subplot(131);
    handleSlice = imagesc(vasculature.rawData(:,:,31),'tag','rawDataS');
    axis tight
    axis equal
        try
        title(vasculature.name,'interpreter','none')
    end
    colormap bone
    h131.View = [90 90];
   % sld = uislider(handleFig,'Position',[50 50 150 3]);
    b = uicontrol('Parent',handleFig,'Style','slider','Position',[100,32,200,20],...
        'value',1, 'min',1, 'max',vasculature.numSlices,'tag','sliceSlider','callback',...
        'handleFig=gcf;rawData=handleFig.UserData;b=findobj(gcf,''tag'',''sliceSlider'');currSlice = round(b.Value);currSlice=max(1,currSlice);currSlice=min(currSlice,size(rawData,3));bl4=findobj(gcf,''tag'',''sliceNumber'');bl4.String=num2str(currSlice);handleSlice=findobj(gcf,''tag'',''rawDataS'');handleSlice.CData = rawData(:,:,currSlice);');
    
    
    
    bgcolor = handleFig.Color;
    bl1 = uicontrol('Parent',handleFig,'Style','text','Position',[80,30,23,23],...
        'String','1','BackgroundColor',bgcolor);
    bl2 = uicontrol('Parent',handleFig,'Style','text','Position',[310,30,23,23],...
        'String',num2str(vasculature.numSlices),'BackgroundColor',bgcolor);
    bl3 = uicontrol('Parent',handleFig,'Style','text','Position',[170,4,100,23],...
        'String','axial slice','BackgroundColor',bgcolor);
    bl1 = uicontrol('Parent',handleFig,'Style','text','Position',[80,30,23,23],...
        'String','1','BackgroundColor',bgcolor);
    bl4 = uicontrol('Parent',handleFig,'Style','edit','Position',[195,55,23,23],...
        'String','1','BackgroundColor',bgcolor,'tag','sliceNumber','callback',...
        'handleFig=gcf;rawData=handleFig.UserData;bl4=findobj(gcf,''tag'',''sliceNumber'');currSlice = round(str2num(bl4.String));currSlice=max(1,currSlice);currSlice=min(currSlice,size(rawData,3));b=findobj(gcf,''tag'',''sliceSlider'');b.Value=currSlice;handleSlice=findobj(gcf,''tag'',''rawDataS'');handleSlice.CData = rawData(:,:,currSlice);');
    
    
    
    sagD = permute(vasculature.rawData,[3 1 2]);
    corD = permute(vasculature.rawData,[3 2 1]);

    h331=subplot(332);
    imagesc((max(vasculature.rawData,[],3)));        axis tight;    axis equal
    h331.View = [ 90 90];
    h332=subplot(335);
    imagesc((max(sagD,[],3)));        axis tight;    axis equal; axis xy
    h333=subplot(338);
    imagesc((max(corD,[],3)));        axis tight;    axis equal; axis xy
    
    
    %if exist('vasculature.name','var')

    
    h133=subplot(133);
    se = strel('sphere',2);
    if isfield(vasculature,'mainRegions')
        fColor = [1 0 0; 0 0 1; 0 1 1;1 1 0;1 0 1;0.5 0.5 1;0.5 1 0.5];
        [f,v]   = isosurface(vasculature.vessels,0.05);
        [f2,v2] = isosurface(vasculature.skeleton,0.05);
        [f3,v3] = isosurface(imdilate(vasculature.branchPoints,se),0.05);
        
       % hPatch  = patch('Faces',f,'Vertices',v,'edgecolor','none','facecolor',0.7*[1 1 1]);
        hPatch2 = patch('Faces',f2,'Vertices',v2,'edgecolor','none','facecolor','k');
        hPatch3 = patch('Faces',f3,'Vertices',v3,'edgecolor','none','facecolor','g');
        hPatch.FaceAlpha = 0.2;
        k2=0;
        for k=1:vasculature.totRegions
            [fr,vr]= isosurface(vasculature.vesselsL==k,0.05);
            if isempty(intersect(k,vasculature.mainRegions))      
                hPatch4 = patch('Faces',fr,'Vertices',vr,'edgecolor','none','facecolor',0.7*[1 1 1]);
            else
                k2=k2+1;
                hPatch4 = patch('Faces',fr,'Vertices',vr,'edgecolor','none','facecolor',fColor(k2,:));
               
            end
            hPatch4.FaceAlpha = 0.2;
        end
  

        
        
    else
        [f,v]   = isosurface(vasculature.vessels,0.05);
        [f2,v2] = isosurface(vasculature.skeleton,0.05);
        [f3,v3] = isosurface(imdilate(vasculature.branchPoints,se),0.05);
        
        %subplot(122)
        hPatch = patch('Faces',f,'Vertices',v,'edgecolor','none','facecolor','r');
        hPatch2 = patch('Faces',f2,'Vertices',v2,'edgecolor','none','facecolor','k');
        hPatch3 = patch('Faces',f3,'Vertices',v3,'edgecolor','none','facecolor','g');
    end
    lighting phong
    camlight left
    view(178,6)
    
    camlight right   
    axis tight
    view(15,80)
    camlight left
    axis ij
    title(strcat('Regions:',32,num2str(vasculature.numRegions),'/',num2str(vasculature.totRegions)))
    rotate3d on
    axis tight
    axis equal
    grid on
    
    %%
    
    h131.Position=[0.03 0.19 0.28 .81];
    %h132.Position=[0.35 0.19 0.28 .81];

    %%
    h331.Position= [0.29      0.55   0.37    0.37];
    h332.Position= [0.35      0.27   0.28    0.28];
    h333.Position= [0.35      0.01   0.28    0.28];
    
    
        h133.Position=[0.66 0.15 0.32 .81];
    
    
    
    