import { Component,OnInit,Input } from '@angular/core';
import {Quote} from '../quote'
@Component({
  selector: 'app-quote',
  templateUrl: './quote.component.html',
  styleUrls: ['./quote.component.css']
})
export class QuoteComponent implements OnInit {

  quotes = [
        new Quote(1,'In the middle of every difficulty lies opportunity');
        new Quote(2,'Life is a beautiful struggle');
        new Quote(3,'Big jobs usually go to the men who prove their ability to outgrow small ones');
      ]
  @Input()quote:Quote;
  constructor() { }

  ngOnInit() {
  }

}
