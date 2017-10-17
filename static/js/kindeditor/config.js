
KindEditor.ready(function(K) {
                window.editor = K.create('#id_text', {
                    width:'800px',
                    height:'400px',
                    uploadJson: '/admin/upload/kindeditor/',
                    afterBlur: function () {
                        this.sync();
                    }
                });
        });