var serverendpoints = $.config.getString("serverendpoints");
var taconfig = $.config.getString("taconfig");
var serverendpointsarr = serverendpoints.split(",");
var languages = $.config.getString("languages");
var mime_type = $.config.getString("mimetype");
var encoding = $.config.getString("encoding");
var recursive =$.config.getString("recursive");
var folderpath = $.config.getString("folderpath");

var tareq = {};   
    
$.setPortCallback("input",onInput);


function gen(ctx) {
    var randomendpoint = serverendpointsarr[Math.floor(Math.random() * serverendpointsarr.length)];
    tareq.folderpath = folderpath;
    tareq.recursive_flag = recursive;
    tareq.document_id = 0;
    tareq.endpoint = randomendpoint;
    tareq.taconfig = taconfig;
    tareq.languages = languages;
    tareq.mime_type = mime_type;
    tareq.text_encoding = encoding;
    if(folderpath)
    {
        var serializedreq = JSON.stringify(tareq);
        console.log("TA Request Creator:\n" + serializedreq+ "\n");
        $.output(serializedreq);
        $.done();
    }
}
$.addGenerator(gen)


function onInput(ctx,s) {
    var randomendpoint = serverendpointsarr[Math.floor(Math.random() * serverendpointsarr.length)];
    tareq.endpoint = randomendpoint;
    tareq.document = s;
    var serializedreq = JSON.stringify(tareq);
    console.log("TA Request Creator:\n" + serializedreq+ "\n");
    $.output(serializedreq);
}