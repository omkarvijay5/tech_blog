function ArticleListController($scope, $resource, ArticleListService) {
    var ctrl = this;

    ctrl.articles = ArticleListService.get_articles().
    then(function success(response) {
        var articles = response.data;
        if (articles.length > 0) {
            var min = 0
            var max = articles.length - 1
            random_index = Math.round(Math.random() * (max - min) + min, 1);
            ctrl.random_article = articles[random_index]
            articles.splice(random_index, 1)
            ctrl.articles = articles
            console.log(random_index)
        } else {
            ctrl.articles = articles
            ctrl.random_article = null
        }
    });
}

angular
  .module('blog')
  .controller('ArticleListController', ArticleListController)
