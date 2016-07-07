'use strict';

angular.module('todoWebApp')
    .service('TodoService', function ($http) {
        return {
            list: function () {
                return $http.get('/dev/api/todo');
            },

            add: function (task) {
                return $http.post('/dev/api/todo', {
                    task: task
                });
            },

            update: function (task_id, task) {
                return $http.put('/dev/api/todo/' + task_id, task);
            },

            remove: function (task_id) {
                return $http.delete('/dev/api/todo/' + task_id);
            },

            clearCompleted: function () {
                return $http.delete('/dev/api/todo?done=true');
            },

            markAllComplete: function () {
                return $http.put('/dev/api/todo');
            }
        }
    });