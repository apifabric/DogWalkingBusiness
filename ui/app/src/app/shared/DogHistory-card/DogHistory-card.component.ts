import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DogHistory-card.component.html',
  styleUrls: ['./DogHistory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DogHistory-card]': 'true'
  }
})

export class DogHistoryCardComponent {


}