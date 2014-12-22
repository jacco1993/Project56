$(document).ready(function()
{
  $('.button').click(function()
  {
      $.ajax(
      {
          url: "json_data.json",
          dataType: "json",
          success: function()
          {
            var json = $.parseJSON('{"beschrijving": [{"name": "Temperatuur, in bedrijf", "value": " 0 - 85 .C"}, {"name": "Temperatuur bij opslag", "value": " -25 - 95 .C"}, {"name": "Intern geheugentype", "value": " DDR2"}, {"name": "CAS-latentie", "value": " 6"}, {"name": "Verpakkingstype", "value": " SO-DIMM"}, {"name": "Intern geheugen", "value": " 4 GB"}, {"name": "Component voor", "value": " Notebook"}, {"name": "Geheugenlayout (modules x formaat)", "value": " 2 x 2 GB"}, {"name": "Ondersteunt Windows", "value": " Y"}, {"name": "Ondersteunt Linux", "value": " Y"}, {"name": "Ondersteunt Mac-besturingssysteem", "value": " Y"}, {"name": "Mac-compatibiliteit", "value": " Y"}, {"name": "Kloksnelheid geheugen", "value": " 800 MHz"}], "price": "64,99", "description": "[KenmerkenTemperatuur, in bedrijf: 0 - 85 c2b0CTemperatuur bij opslag: -25 - 95 c20CIntern geheugentype: DDR2CAS-latentie: 6Verpakkingstype: SO-DIMMIntern geheugen: 4 GBComponent voor: NotebookGeheugenlayout (modules x formaat): 2 x 2 GBOndersteunt Windows: YOndersteunt Linux: YOndersteunt Mac-besturingssysteem: YMac-compatibiliteit: YKloksnelheid geheugen: 800 MHz]", "specs": [{"name": "Besturingssysteem", "value": "Mac"}, {"name": "Platform", "value": "Windows"}, {"name": "Systeemeisen", "value": "Mac compatibel| compatibele besturingssystemen"}, {"name": "Artikelnummer", "value": "CT2C2G2S800MCEU"}, {"name": "EAN", "value": "0649528762368"}], "Title": "4GB kit (2GBx2) DDR2 800MHz (PC2-6400) CL6 SODIMM 200 pin for Mac"}');
            if($("#searchBar").val() == '4' || $("#searchBar").val() == 'GB' || $("#searchBar").val() == "4GB")
            {
              $('#results').html('<div class = "large-12 columns"><div class = "panel"><div class = "text-center"><h4>'+ json.Title + '</h4></div></div></div>' + '<br />' 
                + '<div class = "text-right">€' + json.price + '</div><br />'
                + '<div class = "large-12 columns"><div class = "panel"><div class = "text-center"><h5>Beschrijving</h5></div></div></div><p /><br />'
                + '<h5>' + json.beschrijving[0].name + '</h5>' + json.beschrijving[0].value + '<br />'
                + '<h5>' + json.beschrijving[1].name + '</h5>' + json.beschrijving[1].value + '<br />'
                + '<h5>' + json.beschrijving[2].name + '</h5>' + json.beschrijving[2].value + '<br />'
                + '<h5>' + json.beschrijving[3].name + '</h5>' + json.beschrijving[3].value + '<br />'
                + '<h5>' + json.beschrijving[4].name + '</h5>' + json.beschrijving[4].value + '<br />'
                + '<h5>' + json.beschrijving[5].name + '</h5>' + json.beschrijving[5].value + '<br />'
                + '<h5>' + json.beschrijving[6].name + '</h5>' + json.beschrijving[6].value + '<br />'
                + '<h5>' + json.beschrijving[7].name + '</h5>' + json.beschrijving[7].value + '<br />'
                + '<h5>' + json.beschrijving[8].name + '</h5>' + json.beschrijving[8].value + '<br />'
                + '<h5>' + json.beschrijving[9].name + '</h5>' + json.beschrijving[9].value + '<br />'
                + '<h5>' + json.beschrijving[10].name + '</h5>' + json.beschrijving[10].value + '<br />'
                + '<h5>' + json.beschrijving[11].name + '</h5>' + json.beschrijving[11].value + '<br />'
                + '<h5>' + json.beschrijving[12].name + '</h5>' + json.beschrijving[12].value + '<br />'
                + '<div class = "large-12 columns"><div class = "panel"><div class = "text-center"><h5>Systeem Compatibiliteit</h5></div></div></div><p /><br />'
                + '<h5>' + json.specs[0].name + '</h5>' + json.specs[0].value + '<br />'
                + '<h5>' + json.specs[1].name + '</h5>' + json.specs[1].value + '<br />'
                + '<h5>' + json.specs[2].name + '</h5>' + json.specs[2].value + '<br />'
                + '<div class = "large-12 columns"><div class = "panel"><div class = "text-center"><h5>Artikel</h5></div></div></div><p /><br />'
                + '<h5>' + json.specs[3].name + '</h5>' + json.specs[3].value + '<br />'
                + '<h5>' + json.specs[4].name + '</h5>' + json.specs[4].value);
            }
            else
            {
              $('#results').html('We could not find any products with the input: ' + $("#searchBar").val());
            }
          }
        });
  });
});