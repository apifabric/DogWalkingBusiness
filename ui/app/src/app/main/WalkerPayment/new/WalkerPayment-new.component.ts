import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkerPayment-new',
  templateUrl: './WalkerPayment-new.component.html',
  styleUrls: ['./WalkerPayment-new.component.scss']
})
export class WalkerPaymentNewComponent {
  @ViewChild("WalkerPaymentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}