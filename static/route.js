var blog = angular.module('blog', ["ngRoute", "ngResource"]);


var TEMPLATE_CONFIG = '/static/templates/'

blog.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl: TEMPLATE_CONFIG + "blog/articles.html",
        controller: 'ArticleListController',
        controllerAs: '$ctrl'
    }).
    otherwise({redirectTo: '/'})
    .when("/articles/:id", {
        templateUrl: TEMPLATE_CONFIG + "blog/article_detail.html",
        controller: 'ArticleDetailController',
        controllerAs: '$ctrl'
    }).
    otherwise({redirectTo: '/'})
});