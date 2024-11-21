import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DogHistory-new',
  templateUrl: './DogHistory-new.component.html',
  styleUrls: ['./DogHistory-new.component.scss']
})
export class DogHistoryNewComponent {
  @ViewChild("DogHistoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}