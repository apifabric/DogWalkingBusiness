import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerPaymentHomeComponent } from './home/WalkerPayment-home.component';
import { WalkerPaymentNewComponent } from './new/WalkerPayment-new.component';
import { WalkerPaymentDetailComponent } from './detail/WalkerPayment-detail.component';

const routes: Routes = [
  {path: '', component: WalkerPaymentHomeComponent},
  { path: 'new', component: WalkerPaymentNewComponent },
  { path: ':id', component: WalkerPaymentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkerPayment-detail-permissions'
      }
    }
  }
];

export const WALKERPAYMENT_MODULE_DECLARATIONS = [
    WalkerPaymentHomeComponent,
    WalkerPaymentNewComponent,
    WalkerPaymentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerPaymentRoutingModule { }