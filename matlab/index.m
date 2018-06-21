%% =============== Part 1: Loading dataset ================
clc;clear;close all;

fprintf('Loading dataset.\n\n');
%  Load data
load ('data_diseases.mat');

%  Y is a num_diseases x num_users matrix, containing ratings (age of happening)
%  of num_disease diseases on num_users users
%
%  R is a num_diseases x num_users matrix, where R(i,j) = 1 if and only if user j gave a
%  rating to disease i

%  From the matrix, we can compute statistics like average rating.
%  measure of common-ness
fprintf('Average rating for disease 1 (Malaria): %.4f / 1\n', ...
    mean(R(1, :)));
fprintf('Average age for disease 1 (Malaria): %.0f \n\n', ...
    mean(Y(1, R(1, :))));

%  TODO uncomment
%  We can "visualize" the ratings matrix by plotting it with imagesc
% imagesc(Y);
% ylabel('Diseases');
% xlabel('Users');

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;

%% ============ Part 2: Collaborative Filtering Cost Function ===========

%  Load pre-trained weights (X, Theta, num_users, num_diseases, num_features)
load ('data_diseaseParams.mat');

%  TODO
%  Reduce the data set size so that this runs faster
% num_users = 4; num_diseases = 5; num_features = 3;
% X = X(1:num_diseases, 1:num_features);
% Theta = Theta(1:num_users, 1:num_features);
% Y = Y(1:num_diseases, 1:num_users);
% R = R(1:num_diseases, 1:num_users);

%  Evaluate cost function
J = cofiCostFunc(Theta(:), X, Y, R, num_users, num_features, 0);

fprintf(['Cost at loaded parameters: %f '...
    '\n(cost value should be low)\n'], J);

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;


%% ============== Part 3: Collaborative Filtering Gradient ==============

fprintf('\nChecking Gradients (without regularization) ... \n');

%  Check gradients by running checkNNGradients
checkCostFunction;

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;


%% ========= Part 4: Collaborative Filtering Cost Regularization ========
%  Now, you should implement regularization for the cost function for
%  collaborative filtering. You can implement it by adding the cost of
%  regularization to the original cost computation.
%

lambda = [0.0, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 10, 30, 100];

fprintf('Lambda : \t Cost : \n\n');

for i=1:length(lambda)
    J = cofiCostFunc(Theta(:), X, Y, R, num_users, ...
        num_features, lambda(i));
    
    fprintf('%f \t %f \n', lambda(i), J);
end

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;


%% ======= Part 5: Collaborative Filtering Gradient Regularization ======
%  Once your cost matches up with ours, you should proceed to implement
%  regularization for the gradient.

fprintf('\nChecking Gradients (with regularization) ... \n');

%  Check gradients by running checkNNGradients
checkCostFunction(1.5);

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;


%% ============== Part 6: Entering ratings for a new user ===============
%  Before we will train the collaborative filtering model, we will first
%  add ratings that correspond to a new user that we just observed.

diseaseList = loadDiseaseList();

%  Initialize my ratings
my_ratings = zeros(num_diseases, 1);

% Check the file disease_ids.txt for id of each disease in our dataset
my_ratings(1) = 7;
my_ratings(4) = 26;
my_ratings(5) = 34;

% TODO
my_age = 20;
my_X = rand(1, 2);

fprintf('\n\nNew user ratings:\n');
for i = 1:length(my_ratings)
    if my_ratings(i) > 0
        fprintf('Rated %d for %s\n', my_ratings(i), ...
            diseaseList{i});
    end
end

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;


%% ================== Part 7: Learning Disease Ratings ====================
%  Now, you will train the collaborative filtering model on a disease rating
%  dataset of num_diseases diseases and num_users users

fprintf('\nTraining collaborative filtering...\n');

%  Load data
load('data_diseases.mat');

%  Add our own ratings to the data matrix
Y = [my_ratings, Y];
R = [(my_ratings ~= 0), R];

%  Normalize Ratings
[Ynorm, Ymean] = normalizeRatings(Y, R);

%  Useful Values
% num_features already defined in .mat file
num_users = size(Y, 2);
num_diseases = size(Y, 1);

% Set Initial Parameters - Theta
% TODO X from another .mat file =================================
X = rand(num_diseases, num_features);
Theta = randn(num_users, num_features);

initial_parameters = Theta(:);

% Set options for fmincg
options = optimset('GradObj', 'on', 'MaxIter', 100);

% Set Regularization
lambda = 10;
fmin_theta = fmincg (@(t)(cofiCostFunc(t, X, Ynorm, R, num_users, ...
    num_features, lambda)), ...
    initial_parameters, options);

% Unfold the returned theta back into Theta
Theta = reshape(fmin_theta, num_users, num_features);

fprintf('Recommender system learning completed.\n');

fprintf('\nProgram paused. Press enter to continue.\n');
% pause;

%% ================== Part 8: Recommendation for you ====================
%  After training the model, you can now make recommendations by computing
%  the predictions matrix.
%

p = X * Theta';
my_predictions = p(:,1) + Ymean;

diseaseList = loadDiseaseList();

count = 0;
[r, ix] = sort(my_predictions, 'ascend');
fprintf('\nTop recommendations for you:\n');
fprintf('Predicted rating \n \t(Age) \t\t Disease \n\n');
for i=1:num_diseases
    j = ix(i);
    
    if my_predictions(j) >= my_age && norm(X(j, :) - my_X) <= 0.3
        fprintf('\t %.0f \t\t (%.2f %%) %s\n', my_predictions(j),100*(1 - norm(X(j,:) - my_X)), diseaseList{j});
        count = count + 1;
    end
end

if count == 0
    disp('Oops..No matching data found');
end

% fprintf('\nTop recommendations for you:\n');
% fprintf('Predicted rating \n \t(Age) \t\t Disease \n\n');
% for i=1:num_diseases
%     j = i;
%
%     if my_predictions(j) >= my_age && norm(X(j, :) - my_X) <= 0.3
%         fprintf('\t %.0f \t\t %s\n', my_predictions(j), diseaseList{j});
%     end
% end

fprintf('\n\nOriginal ratings provided:\n');
for i = 1:length(my_ratings)
    if my_ratings(i) > 0
        fprintf('Rated %d for %s\n', my_ratings(i), ...
            diseaseList{i});
    end
end
