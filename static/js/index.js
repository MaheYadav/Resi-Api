$('.apireq').click( function() {
    $.ajax({ 
             type:'GET'
             url : "{% studentsapi %}",
             dataType: "json",
             success : function (data) {
                      $('#id').text( data[0].id);
                      $('#first_name').text( data[0].first_name);
                      $('#last_name').text( data[0].last_name);
                      $('#age').text( data[0].age);
                      $('#gender').text( data[0].gender);
                    }
                 });
             });
