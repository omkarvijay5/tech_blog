var blog = angular.module('blog')

blog.factory('RandomArticleService', function($http) {
  var data = {};
  data.get_articles = function () {
    return $http({
        method : "GET",
        url : "/api/v1/blog/random/articles/"
    })
  }
  return data
});
