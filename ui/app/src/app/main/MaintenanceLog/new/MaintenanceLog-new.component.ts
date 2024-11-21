import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'MaintenanceLog-new',
  templateUrl: './MaintenanceLog-new.component.html',
  styleUrls: ['./MaintenanceLog-new.component.scss']
})
export class MaintenanceLogNewComponent {
  @ViewChild("MaintenanceLogForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}