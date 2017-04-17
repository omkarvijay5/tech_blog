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
