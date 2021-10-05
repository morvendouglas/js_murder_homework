// Ep 1 = The murderer is Miss Scarlet.
// Ep 2 = The murderer is Professor Plum. 
// Ep 3 = First Verdict: The murderer is Mrs. Peacock. 
//        Second Verdict: The murderer is Professor Plum.
// Ep 4 = The suspects are Miss Scarlet, Professor Plum, Colonel Mustard.
//        Suspect three is Mrs. Peacock.
// Ep 5 = The weapon is the Revolver.
// Ep 6 = The murderer is Mrs White.
// Ep 7 = The murderer is Mr Green.
// Ep 8 = The weapon is Candle Stick.
// Ep 9 = The murderer is Professor Plum.

// Ep 2
// const murderer = 'Professor Plum';

// const changeMurderer = function() {
//     var murderer = 'Mrs. Peacock';
// }

// const declareMurderer = function() {
//   return `The murderer is ${murderer}.`;
// }

// changeMurderer();
// const verdict = declareMurderer();
// console.log(verdict);


// MINE

var murderer = 'Ted Bundy'

const plotChange = function(){
    let murderer = 'Dan Scott'
    return murderer
}

plotChange()

const anotherPlotChange = function(name){
    let murderer = name
    return murderer
};

var newMurderer = anotherPlotChange('Charles Manson')
console.log(newMurderer)

var foundMurderer = function(){
    return `${murderer} is following you...`
}

var suspects = foundMurderer()
console.log(suspects)








  