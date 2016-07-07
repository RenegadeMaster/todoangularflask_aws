'use strict';

angular.module('todoWebApp')
    .controller('TodosCtrl', function($scope, TodoService) {
        $scope.items = [];
        $scope.pendingItems = []
        $scope.completedItems = [];
        $scope.itemsLeftCounter = 0;
        $scope.newTodo = '';
        $scope.editingTodo = -1;
        $scope.selectedFilter = 'all';

        TodoService.list().then(function (result) {
            if (result.data.constructor === Array) {
                $scope.items = result.data;
                $scope.itemsLeftCounter = $scope.items.reduce(function (prev, current, index, array) {
                    if (!array[index].done) {
                        return prev + 1;
                    }
                    return prev;
                }, 0);
            }
        });

        $scope.addTodo = function () {
            var task = $scope.newTodo.trim();
            if (task === '') {
                return;
            }
            TodoService.add(task)
                .then(function (result) {
                    $scope.items.push(result.data);
                    $scope.itemsLeftCounter += 1;
                    $scope.newTodo = '';
                });
        };

        $scope.toggleTodo = function (todo_id, index) {
            TodoService.update(todo_id, {done: !$scope.items[index]['done']})
                .then(function () {
                    $scope.items[index]['done'] = !$scope.items[index]['done'];
                    if ($scope.items[index]['done']) {
                        $scope.itemsLeftCounter -= 1;
                    } else {
                        $scope.itemsLeftCounter += 1;
                    }
                });
        };

        $scope.removeTodo = function (todo_id, index) {
            TodoService.remove(todo_id).then(
                function() {
                    $scope.items.splice(index, 1);
                }
            );
        };

        $scope.editTodo = function (todo_id) {
            $scope.editingTodo = todo_id;
        };

        $scope.doneEditingTodo = function (todo_id, index) {
            TodoService.update(todo_id, {task: $scope.items[index]['task']})
                .then(function () {
                   $scope.closeEditingTodo();
                });
        };

        $scope.closeEditingTodo = function () {
            $scope.editingTodo = -1;
        };

        $scope.clearCompleted = function () {
            TodoService.clearCompleted()
                .then(function() {
                   $scope.items = $scope.items.filter(function (el) {
                       return !el.done;
                   });
                   $scope.itemsLeftCounter = $scope.items.length;
                });
        };

        $scope.markAllComplete = function () {
            TodoService.markAllComplete()
                .then(function () {
                    $scope.items.forEach(function(el) {
                        el.done = true;
                    });
                });
        }
    });