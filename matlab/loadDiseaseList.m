function diseaseList = loadDiseaseList()
%GETDISEASELIST reads the fixed disease list in disease_ids.txt and returns a
%cell array of the words
%   diseaseList = GETDISEASELIST() reads the fixed disease list in disease_ids.txt 
%   and returns a cell array of the words in diseaseList.


%% Read the fixed disease list
fid = fopen('disease_ids.txt');

% Store all movies in cell array disease{}
%  TODO
n = 1682;  % Total number of disease 

diseaseList = cell(n, 1);
for i = 1:n
    % Read line
    line = fgets(fid);
    % Word Index (can ignore since it will be = i)
    [idx, diseaseName] = strtok(line, ' ');
    % Actual Word
    diseaseList{i} = strtrim(diseaseName);
end
fclose(fid);

end
