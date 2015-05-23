define(function (require) {

    "use strict";

    var Backbone = require('backbone'),
        Model    = require('noteDetails/models/noteDetailsModel'),
        tpl      = require('text!noteDetails/tpl/noteDetailsTpl.html'),

        template = _.template(tpl);

    return Backbone.View.extend({

        model: null,

        initialize: function(options) {
            console.log("init");
            if(options) {
                this.model = new Model(options);
                this.fetchDetails();
            }
            else {
                this.model = new Model();
                this.render();
            }
        },

        events: {
            "click #submit" : "submitDetails"
        },

        submitDetails: function() {
            var self = this;

            $('#msg').html('');

            this.model.attributes.title = $('#title', this.$el).val();
            this.model.attributes.description = $('#description', this.$el).html();

            this.model.save({
                success: function (data) {
                        document.router.navigate("", {trigger: true, replace: true});
                },
                error: function (data) {
                    $('#msg').html('Failed to save details.');
                }
            });

        },

        fetchDetails: function() {
            var self = this;

            console.log("fetch");
            this.model.fetch({
                success: function (data) {
                        self.render();
                },
                error: function (data) {
                    self.render();
                    $('#msg').html('Failed to load details.');
                }
            });

        },

        render: function () {
            console.log("render");
            this.$el.html(template(this.model.attributes));
            return this;
        }
 
    });

});