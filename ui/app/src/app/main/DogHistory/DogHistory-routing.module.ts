import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DogHistoryHomeComponent } from './home/DogHistory-home.component';
import { DogHistoryNewComponent } from './new/DogHistory-new.component';
import { DogHistoryDetailComponent } from './detail/DogHistory-detail.component';

const routes: Routes = [
  {path: '', component: DogHistoryHomeComponent},
  { path: 'new', component: DogHistoryNewComponent },
  { path: ':id', component: DogHistoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DogHistory-detail-permissions'
      }
    }
  }
];

export const DOGHISTORY_MODULE_DECLARATIONS = [
    DogHistoryHomeComponent,
    DogHistoryNewComponent,
    DogHistoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DogHistoryRoutingModule { }