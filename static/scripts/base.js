//static/scripts/base.js
class Base{
  constructor(){
    this.setDate();
  }

  toKhNum(number){
    var numObj = {0:'០',1:'១',2:'២',3:'៣',4:'៤',5:'៥',6:'៦',7:'៧',8:'៨',9:'៩'};
    number = number+'';
    var strNumber = '';

    for( var v in number)
      strNumber += numObj[parseInt(number[v])];
    
    return strNumber;
  }

  setDate(){
    this.KhmerDays = ['អាទិត្យ', 'ច័ន្ទ', 'អង្គារ', 'ពុធ', 'ព្រហស្បតិ៍', 'សុក្រ', 'សៅរ៍'];
    this.KhmerMonths = ['មករា', 'កុម្ភៈ', 'មិនា', 'មេសា', 'ឧសភា', 'មិថុនា', 'កក្កដា', 'សីហា', 'កញ្ញា', 'តុលា', 'វិច្ឆិកា', 'ធ្នូ'];
    var date = new Date();
    this.month = date.getMonth();
    this.day = date.getDay();
    this.daym = this.toKhNum(date.getDate());
    this.year = this.toKhNum(date.getFullYear());
    this.time = date.toLocaleTimeString();
    return ('ថ្ងៃ '+this.KhmerDays[this.day]+' ទី '+this.daym+' '+this.KhmerMonths[this.month]+' '+this.year)
  }

  setClock(){
    var period = 'ព្រឹក';
    var today = new Date();
    var h = today.getHours();
    if(h>12){
      h = h-12;
      period = 'ល្ងាច';
    }
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = base.checkTime(m);
    s = base.checkTime(s);
  
    document.getElementById('kh-clock').innerHTML = "ម៉ោង "+base.toKhNum(h) + "ៈ" + base.toKhNum(m) + "ៈ" + base.toKhNum(s)+' '+period;
    var t = setTimeout(base.setClock, 500);
  }

  checkTime(i){
    if (i < 10){i = "0" + i};  
    return i;
  }

  mobileMenu(){
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav")
      x.className += " responsive";
    else
      x.className = "topnav";
  }
}//end of class
