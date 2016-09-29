define(['angular', './sample-module'], function(angular, sampleModule) {
    'use strict';
    return sampleModule.controller('SampleCtrl', ['$scope', '$http', function($scope, $http) {

        function consumeService($scope, $http){
            $http({
                method: 'GET',
                url: 'https://jsonparse.run.aws-usw02-pr.ice.predix.io/',
                headers: {
                }
            }).
            success(function(data){
                $scope.data = data;
            });
        }
        consumeService($scope, $http);
    }]);
});
