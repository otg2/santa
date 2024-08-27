

var names = ["Ottar", "Magnus", "Knutur", "Vidar", "Atli", "Kriss", "Dabbi", "Hrodmar", "Erling", "Gunnar", "Petur"]

var leynivin = ["Ottar", "Magnus", "Knutur", "Vidar", "Atli", "Kriss", "Dabbi", "Hrodmar", "Erling", "Gunnar", "Petur"]


var pairs = [];

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}


names = shuffle(names);
leynivin = shuffle(leynivin);

var increment = 0 ;
var isComplete = false;

while(!isComplete)
{
	increment++;
	names = shuffle(names);
	leynivin = shuffle(leynivin);
	
	isComplete = true;
	
	for(var i = 0; i < names.length; i++)
	{
		if(names[i] === leynivin[i])
		{
			isComplete = false;
		}
	}
	
	for(var i = 0; i < a.length; i++)
	{
		var firstLink = names[i];
		var secondLink = leynivin[i];
		
		var indexOfA = names.indexOf(secondLink)
		
		if(leynivin[indexOfA] === firstLink)
		{
			isComplete = false;
		}
	}
}

console.log("santa sort in ", increment);

console.log(names);
console.log(leynivin);

var fso = new ActiveXObject("Scripting.FileSystemObject");
    var fh = fso.OpenTextFile("data.txt", 8, false, 0);
    fh.WriteLine("testest");
    fh.Close();
