var blog = angular.module('blog')

blog.factory('ArticleListService', function($http) {
  var data = {};
  data.get_articles = function () {
    return $http({
        method : "GET",
        url : "/api/v1/blog/articles/"
    })
  }
  return data
});
