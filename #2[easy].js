/*
An important part of programming is being able to apply your programs, 
so your challenge for today is to create a calculator application that has use in your life. 
It might be an interest calculator, or it might be something that you can use in the classroom. 
For example, if you were in physics class, you might want to make a F = M * A calc.
*/

var units=prompt("Press 'cm' if you want to convert centimeters to inches or 'i' if you want to convert inches to  centimeters");

function metricToImperial(centimeters){
    return Math.round(centimeters*0.394* 100) / 100;
}

function imperialToMetric(inches){
    return Math.round(inches*2.54* 100) / 100;   
}

var value=prompt("Insert value");

if(units==='cm'){
    metricToImperial(value);
}else if(units==='i'){
    imperialToMetric(value);
}else{
    console.log("Did you type something other than 'cm' or 'i'?");
}
