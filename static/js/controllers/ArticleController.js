function ArticleListController($scope, $resource, ArticleListService) {
    var ctrl = this;

    ctrl.articles = ArticleListService.get_articles().
    then(function success(response) {
        ctrl.articles = response.data;
        console.log(ctrl.articles)
    });
}

angular
  .module('blog')
  .controller('ArticleListController', ArticleListController)
