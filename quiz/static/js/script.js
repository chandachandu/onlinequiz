      $(document).ready(function() {
            pageid=1;
            var x=questiondata(pageid);
            var data;
          function questiondata(page_n) {
              $("input[name=answer]").removeAttr('disabled');
              $("input[name=answer]").prop("checked",false);
                $('.errortag').remove();
                $.ajax({
                type: "POST",
                url: window.location.href, // name of url
                data : {
                page_n : page_n, //page_number
                csrfmiddlewaretoken: '{{ csrf_token }}',
            },
            success: function (resp) {
                //loop
                data=resp.results[0]
                $('#question_id').text(page_n)
                $('#question_data').text(data.question)
                $('#option1').val(data.option1)
                $('#optionval1').text(data.option1)
                $('#option2').val(data.option2)
                $('#optionval2').text(data.option2)
                $('#option3').val(data.option3)
                $('#optionval3').text(data.option3)
                $('#option4').val(data.option4)
                $('#optionval4').text(data.option4)
                console.log(data.id);
            },
            error: function () {}
        });
            }


         $("input[name=answer]").click(function () {
             $('.errortag').remove();
                url=window.location.origin+"/result/";
                var answer=$(this).val();
                $('.form-check').addClass('disabled');
                $("input[name=answer]").attr('disabled','disabled');
                $(this).removeAttr('disabled','disabled');
                $.ajax({
                    url:url,
                    type:'POST',
                    data:{'qid':data.id,'answer':answer},
                    dataType: "json",
                    success : function (data){
                        if(data['error']){
                            $('#option_list').after("<p class='text-rose font-weight-bold errortag'>"+data['error']+"</p>");
                            pageid=pageid+1;
                           setTimeout(function() {
                                t=questiondata(pageid);
                            }, 2000);
                        }
                        if(data['success']){
                            $('#option_list').after("<p class='text-info font-weight-bold errortag'>"+data['success']+"</p>");
                            pageid=pageid+1;
                            setTimeout(function() {
                                t=questiondata(pageid);
                            }, 2000);

                        }
                    },
                    failure : function (data) {
                        alert('Got an error');
                    }
                })
          });





      });
