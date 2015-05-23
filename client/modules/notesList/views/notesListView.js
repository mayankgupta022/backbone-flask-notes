define(function (require) {

    "use strict";

    var Backbone    = require('backbone'),
        Collection  = require('notesList/collections/notesListCollection'),
        tpl         = require('text!notesList/tpl/notesListTpl.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        collection: null,

        initialize: function() {
            this.collection = new Collection();
            this.render();
        },

        render: function () {
            var self = this;

            this.collection.fetch({
                success: function (data) {
                        self.$el.html(template(this.collection.models));
                },
                error: function (data, response) {
                    console.log('Failed to load details.');
                    console.log(response);
                }
            });

            return this;
        }
 
    });

});