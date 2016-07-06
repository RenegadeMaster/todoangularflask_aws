'use strict';

angular.module('todoWebApp')
    .directive('ngEnter', function() {
        return function (scope, element, attrs) {
            element.bind('keydown keypress', function (event) {
                if(event.which === 13) { // 13 = Enter KeyCode
                    scope.$apply(function() {
                        scope.$eval(attrs['ngEnter']); // Our directive will take a function as 'parameter'
                    });
                    event.preventDefault();
                }
            });
        };
    });