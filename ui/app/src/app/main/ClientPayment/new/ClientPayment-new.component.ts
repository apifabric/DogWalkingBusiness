import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'ClientPayment-new',
  templateUrl: './ClientPayment-new.component.html',
  styleUrls: ['./ClientPayment-new.component.scss']
})
export class ClientPaymentNewComponent {
  @ViewChild("ClientPaymentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}