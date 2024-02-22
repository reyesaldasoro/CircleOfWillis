function handleFig2 = displayCircleThickness(vasculature)

if isa('vasculature','char')
    vasculature = segment_CircleOfWillis (vasculature,0); 
end
vasculatureThick    = bwdist(vasculature.vessels==0);
vasculatureThick2   = vasculatureThick.*vasculature.skeleton;

if ~isfield(vasculature,'info')
    % try to read the info of the file 
    try
    vasculature.info    = niftiinfo(vasculature.name);
    scalingFactor       = vasculature.info.PixelDimensions(1);
    catch
        scalingFactor   = 1;
    end
else
    scalingFactor       = vasculature.info.PixelDimensions(1);
end
[f,v,c]   = isosurface(vasculatureThick2,0.05,scalingFactor*imdilate(vasculatureThick2,ones(5)));

handleFig2=figure;
patch('Vertices',v,'Faces',f,'FaceVertexCData',c,'FaceColor','interp','EdgeColor','interp')
colormap (jet)
colorbar
grid on
rotate3d on
title(strcat('Scaling Factor = ',num2str(scalingFactor)))