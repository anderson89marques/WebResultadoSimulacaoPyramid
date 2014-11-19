$(document).ready(function(){
    //buscar os dados no servidor e depois mostra o resultado na tela
    function busca_dados(dado){

        $('#lista_resultados').html(" ")
        $("h2").html("Resultados")
        $.ajax({url : "resposta_ajax", data:{nome : dado },
            success: function(valor){
                var l = ""
                for(var i =0;i < valor.lista.length;i++){ //retorno uma lista de dicionários
                    var obj = valor.lista[i] //pego o dicionário de cada posição da lista
                    for(var key in obj){ //pego a chave
                        l += "<li>" + key + " : " + obj[key] + "</li>" // adiciono chave e valor em liste
                    }
                }
                $('#lista_resultados').html(l)

            },
             beforeSend:function(){
                $('#loading').css({display: "block"});
             },
            complete:function(){
                $('#loading').css({display: "none"});
                $("h2").html("Resultados da "+ dado)
            }});

    }

    $('#1').click(function(e){
        //$('#lista_resultado').remove("li");
        busca_dados($(this).text())
    });

    $('#2').click(function(e){
        busca_dados($(this).text())
    });
});