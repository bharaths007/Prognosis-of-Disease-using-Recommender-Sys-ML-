function [J, grad] = cofiCostFunc(Theta, X, Y, R,...
    num_users, num_features, lambda)
%COFICOSTFUNC Collaborative filtering cost function
%   [J, grad] = COFICOSTFUNC(Theta, X, Y, R, lambda) returns the cost and gradient for the
%   collaborative filtering problem.

Theta = reshape(Theta, num_users, num_features);

J = 0;
Theta_grad = zeros(size(Theta));

dif = (((X * Theta') .* R) - Y);

difSqr = dif .^ 2;              
J = (1/2) * sum(difSqr(:));
% Adding Regularization terms for J (i.e cost)
term_thetaSqr = Theta .* Theta;
J = J + (lambda / 2) * sum(term_thetaSqr(:));

Theta_grad = dif' * X; 
% Adding Regularization terms for Theta_grad
Theta_grad = Theta_grad + (lambda * Theta);

% =============================================================

grad = Theta_grad(:);

end
