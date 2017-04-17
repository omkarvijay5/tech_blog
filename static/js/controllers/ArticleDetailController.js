function ArticleDetailController($scope, $routeParams, ArticleDetailService) {
    var ctrl = this;
    var article_id = $routeParams.id

    ctrl.article = ArticleDetailService.get_article(article_id).
    then(function success(response) {
        ctrl.article = response.data;
    
    });
}

angular
  .module('blog')
  .controller('ArticleDetailController', ArticleDetailController)
