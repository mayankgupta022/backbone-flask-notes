define(function (require) {

    "use strict";

    var Backbone = require('backbone');
        
    return Backbone.Collection.extend({

    	url: document.serverURL + 'notes'
        // url: 'http://localhost:84/user/getInfo'
    });

});