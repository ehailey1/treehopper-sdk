//=========================================================
// src/Interrupts.c: generated by Hardware Configurator
//
// This file will be regenerated when saving a document.
// leave the sections inside the "$[...]" comment tags alone
// or they will be overwritten!
//=========================================================

// USER INCLUDES
#include <SI_EFM8UB1_Register_Enums.h>
#include "pwm.h"
#include "softPwm.h"
#include "treehopper.h"

//-----------------------------------------------------------------------------
// TIMER3_ISR
//-----------------------------------------------------------------------------
//
// TIMER3 ISR Content goes here. Remember to clear flag bits:
// TMR3CN0::TF3H (Timer # High Byte Overflow Flag)
// TMR3CN0::TF3L (Timer # Low Byte Overflow Flag)
//
//-----------------------------------------------------------------------------
SI_INTERRUPT (TIMER3_ISR, TIMER3_IRQn) {
	SFRPAGE = 0x00;
	TMR3CN0 &= ~(TMR3CN0_TF3H__SET | TMR3CN0_TF3L__SET);


}

//-----------------------------------------------------------------------------
// PCA0_ISR
//-----------------------------------------------------------------------------
//
// PCA0 ISR Content goes here. Remember to clear flag bits:
// PCA0CN0::CCF0 (PCA Module 0 Capture/Compare Flag)
// PCA0CN0::CCF1 (PCA Module 1 Capture/Compare Flag)
// PCA0CN0::CCF2 (PCA Module 2 Capture/Compare Flag)
// PCA0CN0::CF (PCA Counter/Timer Overflow Flag)
// PCA0PWM::COVF (Cycle Overflow Flag)
//
//-----------------------------------------------------------------------------
SI_INTERRUPT (PCA0_ISR, PCA0_IRQn) {
	SFRPAGE = 0x00;
	if (PCA0CN0_CCF0) {
		PCA0CPL0 = PWM_1L;
		PCA0CPH0 = PWM_1H;
		PCA0CN0_CCF0 = 0;
	}

	if (PCA0CN0_CCF1) {
		PCA0CPL1 = PWM_2L;
		PCA0CPH1 = PWM_2H;
		PCA0CN0_CCF1 = 0;
	}

	if (PCA0CN0_CCF2) {
		PCA0CPL2 = PWM_3L;
		PCA0CPH2 = PWM_3H;
		PCA0CN0_CCF2 = 0;
	}

	PCA0CN0_CF = 0;
	PCA0PWM &= ~PCA0PWM_COVF__OVERFLOW;

}

//-----------------------------------------------------------------------------
// TIMER4_ISR
//-----------------------------------------------------------------------------
//
// TIMER4 ISR Content goes here. Remember to clear flag bits:
// TMR4CN0::TF4H (Timer # High Byte Overflow Flag)
// TMR4CN0::TF4L (Timer # Low Byte Overflow Flag)
//
//-----------------------------------------------------------------------------
SI_INTERRUPT (TIMER4_ISR, TIMER4_IRQn) {
	SFRPAGE = 0x10;
	TMR4CN0 &= ~(TMR4CN0_TF4H__SET | TMR4CN0_TF4L__SET);
	SoftPwm_Task();
}
