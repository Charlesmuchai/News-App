import { Component,OnInit,Input } from '@angular/core';
import {Quote} from '../quote'
@Component({
  selector: 'app-quote',
  templateUrl: './quote.component.html',
  styleUrls: ['./quote.component.css']
})
export class QuoteComponent implements OnInit {

  quotes = [
        new Quote(1,'In the middle of every difficulty lies opportunity!', "blah blah blah")
      ]
  @Input()quote:Quote;
  constructor() { }

  ngOnInit() {
  }

}
