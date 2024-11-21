import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Walker-new',
  templateUrl: './Walker-new.component.html',
  styleUrls: ['./Walker-new.component.scss']
})
export class WalkerNewComponent {
  @ViewChild("WalkerForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}