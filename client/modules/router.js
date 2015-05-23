define(function (require) {

    "use strict";

    var model       = require('common/models/model'),
        ShellView   = require('shell/views/shell'),
        $body       = $('body'),
        shellView,
        currentView,
        $content;

    return Backbone.Router.extend({

        routes: {
            "": "notes",
            "notes": "notes",
            "note/new": "newNote",
            "note/:id": "updateNote",
        },

        initialize: function () {
            shellView = new ShellView();
            $body.html(shellView.render().el);
            $content = $("#content");
        },

        updateCurrentView: function(newView) {
            //COMPLETELY UNBIND THE VIEW
            if(this.currentView) {
                if(typeof this.currentView.close === "function")
                    this.currentView.close();
                this.currentView.undelegateEvents();
                $(this.currentView.el).removeData().unbind(); 
                //Remove currentView from DOM
                this.currentView.remove();  
                Backbone.View.prototype.remove.call(this.currentView);
            }
            this.currentView= newView;
            this.currentView.delegateEvents(); // delegate events when the view is recycled
        },

        notes: function () {
            var self = this;
            require(["notesList/views/notesListView"], function (NotesList) {
                var notesList = new NotesList();
                self.updateCurrentView(notesList);
                $(notesList.el).appendTo($content);
            });
        },

        newNote: function () {
            var self = this;
            require(["noteDetails/views/noteDetailsView"], function (NoteDetails) {
                var noteDetails = new NoteDetails();
                self.updateCurrentView(noteDetails);
                $(noteDetails.el).appendTo($content);
            });
        },

        updateNote: function (id) {
            var self = this;
            require(["noteDetails/views/noteDetailsView"], function (NoteDetails) {
                var noteDetails = new NoteDetails({id: id});
                self.updateCurrentView(noteDetails);
                $(noteDetails.el).appendTo($content);
            });
        },

    });

});