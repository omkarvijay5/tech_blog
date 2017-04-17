var blog = angular.module('blog')

blog.factory('ArticleDetailService', function($http) {
  var data = {};
  data.get_article = function (article_id) {
    return $http({
        method : "GET",
        url : "/api/v1/blog/article/" + article_id.toString()
    })
  }
  return data
});
