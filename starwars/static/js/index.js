$(function() {
    $.get("https://swapi.dev/api/films", function(data){
        var filmsTitle = [];
        films = data.results

        for(let film of films){
            filmsTitle.push(film.title)
        }

        $( "#search_text" ).autocomplete({
            source: filmsTitle
        });
    })
});
