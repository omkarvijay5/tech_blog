var TEMPLATE_CONFIG = '/static/templates/'

function WhatReadNextController($scope, RandomArticleService) {
    var ctrl = this;
    ctrl.random_articles = RandomArticleService.get_articles().
    then(function success(response) {
        ctrl.random_articles = response.data;
    });
}

angular.module('blog').component('whatReadNext', {
  templateUrl: TEMPLATE_CONFIG + 'blog/what_read_next.html',
  controller: WhatReadNextController
});

angular.module('blog').filter('startFrom', function() {
    return function(input, start) {
        if (input.length > 0){
            start = +start; //parse to int
            return input.slice(start);
        } else {
            return []
        }

    }
});
