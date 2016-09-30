define(['angular', './sample-module'], function(angular, sampleModule) {
    'use strict';
    return sampleModule.controller('SampleCtrl2', ['$scope', '$http', function($scope, $http) {
        var sPageURL = window.location.search.substring(1);
        var texto;
        function consumeService($scope, $http){
            $http({
                method: 'GET',
                url: 'https://jsonparse.run.aws-usw02-pr.ice.predix.io/engines',
                headers: {
                }
            }).
            success(function(data){
                $scope.data = data;
            });
        }

        function getAll($scope, $http){
            var param = sPageURL.split("=")[1];
            console.log("fsiohdsofh");
            $http({
                method: 'GET',
                url: 'https://jsonparse.run.aws-usw02-pr.ice.predix.io/all/' + param,
                headers: {
                }
            }).
            success(function(all){
                $scope.all = all;
                console.log(all);
            });
        }

        function getFlight($scope, $http){
            var param = sPageURL.split("=")[1];
            $http({
                method: 'GET',
                url: 'https://jsonparse.run.aws-usw02-pr.ice.predix.io/flights/'+ param,
                headers: {
                }
            }).
            success(function(dets){
                $scope.dets = dets;
            });
        }

        function getCosts($scope, $http){
            var param = sPageURL.split("=")[1];
            $http({
                method: 'GET',
                url: 'https://jsonparse.run.aws-usw02-pr.ice.predix.io/costs/'+ param,
                headers: {
                }
            }).
            success(function(cost){
                $scope.cost = cost;
            });
        }

        if (sPageURL){
            getAll($scope, $http);
            getFlight($scope, $http);
            getCosts($scope, $http);
        }
        consumeService($scope, $http);
        document.getElementById('ddlist').addEventListener('dropdown_content_value_changed', function(e) {
            texto = e.detail;
            $scope.currentESN = texto.textValue;
            location.replace("http://localhost:9000/second?flight=" + $scope.currentESN)
        });
    }]);
});

