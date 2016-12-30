xmlhttp=new XMLHttpRequest();
xmlhttp.open("GET", "https://raw.githubusercontent.com/TurkuNLP/list-of-publications/master/turkunlp.bib", false);
xmlhttp.send();
var entries = BibtexParser(xmlhttp.responseText);
var mytable="<thead><tr><th>Author</th><th>Year</th><th>Title</th></tr></thead>\n<tbody>\n";

console.log(entries["entries"]);
for (eidx in entries["entries"]) {
    var fields=entries["entries"][eidx]["Fields"];
    console.log(fields);
    mytable+="<tr><td>"+fields["Author"]+"</td><td>"+fields["Year"]+"</td><td>"+fields["Title"]+"</td></tr>\n";
}
mytable+="</tbody>";
$("#pubtable").html(mytable)
