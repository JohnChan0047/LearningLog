KindEditor.ready(function(K) {
                window.editor = K.create('#id_text', {
                    width:'800px',
                    height:'400px',
                    uploadJson: '/uploads/kindeditor',
                    afterBlur: function () {
                        this.sync();
                    }
                });
        });