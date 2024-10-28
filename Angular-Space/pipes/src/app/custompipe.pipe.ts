import { Pipe, PipeTransform } from '@angular/core';
import { NavigationStart } from '@angular/router';

@Pipe({
  name: 'custompipe'
})
export class CustompipePipe implements PipeTransform {

  transform(value: string, ...args: unknown[]): unknown {

    var nstr:any;
    var nword:string=''

    nstr=value.split(' ')

    nword=nstr.join('')

    // // nstr=value.replace(' ','')
    // for(var i=0;i<nstr.length;i++){
    //   nword+=nstr[i];
    // }

    // var nstr:string='';

    // for(var i=0;i<value.length;i++){
    //   if(i%2==0)
    //     nstr+=value[i].toUpperCase()
    //   else 
    //     nstr+=value[i].toLowerCase();
    // }
    
    return nword;
  }

}
