c This code calculates the nuclear overlap functions which are needed 
c to scale pp to pA and AB.
c Units are fm.
c TAB is overlap function in 1/fm^2; divide the value by 10 to get it in mb^-1
c scal1 is sigma(A1,A2)/sigma(p,p)
c scal2 is n(A1,A2)/sigma(p,p)
c The calculation is done in steps of 0.1 fm. 
c The cutoff R and b are 10 and 20 fm, respectively.
c D.Miskowiec 1997, updated in 2001. 
*******************************************************************************
      program overlap
      implicit none
      double precision A1,A2
      double precision sigma_NN
      double precision density
      double precision TA,TAB
      double precision b(200),TA1(200),TA2(200),TA1A2(200)
      double precision npart1(200),npart2(200),TA1A2check(200)
      double precision sigma(200),sigmasum(200)
      double precision rmax
      integer denflag,nshot
      common denflag,nshot,rmax
      integer i
      rmax=10.0
      
c Input
c------
      write(*,900)
      write(*,*)'Nuclear overlap calculation'
      write(*,*)'Enter A,B'
      read(*,*)A1,A2
      write(*,*)'Select density profile: 1 for sharp sphere',
     +          ' or 2 for Woods-Saxon'
      read(*,*)denflag
      write(*,*)'Enter sigma_NN in mb'
      read(*,*)sigma_NN
      write(*,*)'Enter number of shots per integral (e.g. 10000)'
      read(*,*)nshot

c Print parameters
c-----------------
      write(*,900)
      write(*,*)'A .................',A1
      write(*,*)'B .................',A2
      write(*,*)'sigma_NN ..........',sigma_NN,' mb'
      write(*,*)'statistics ........ ',nshot
      if (denflag.eq.1) write(*,*)'density profile ...  ','sharp sphere'
      if (denflag.eq.2) write(*,*)'density profile ...  ','Woods-Saxon'
      write(*,900)

c Calculate thickness functions for A1 and A2
c--------------------------------------------
      write(*,*)'Calculating TA for A and B'
      do i=1,200
        b(i)=dble(i)/10.0-0.05
        TA1(i)=TA(A1,b(i))
        TA2(i)=TA(A2,b(i))
      enddo

c Calculate overlap function for A1+A2 collision using densities
c---------------------------------------------------------------
      write(*,*)'Calculating TAB for A+B collision'
      do i=1,200
        TA1A2(i)=TAB(A1,A2,b(i))
      enddo

c Calculate npart and overlap function using thickness functions
c---------------------------------------------------------------
      write(*,*)'Calculating Npart and TAB for A+B collision'
      do i=1,200
        call NPART(A1,A2,b(i),sigma_NN,TA1,TA2,TA1A2check(i),
     +             npart1(i),npart2(i))
      enddo

c Calculate cross section
c------------------------
      write(*,*)'Calculating cross section for A+B collision'
      sigmasum(1)=0.0
      do i=1,200
        sigma(i)=2*3.1416*b(i)*0.1*(1-exp(-sigma_NN*TA1A2check(i)/10))
c       if (TA1A2check(i).gt.0.0d0) sigma(i)=2*3.1416*b(i)*0.1
        sigmasum(i)=sigma(i)
        if (i.gt.1) sigmasum(i)=sigmasum(i)+sigmasum(i-1)
      enddo
      write(*,908)'cross section .....',sigmasum(200)/100,'barn'

c Print legend
c-------------
      write(*,900)
      write(*,*)'b ................. impact parameter or radius (fm)'
      write(*,*)'nA ................ density of nucleus A (1/fm^3)'
      write(*,*)'nB ................ density of nucleus B (1/fm^3)'
      write(*,*)'TA ................ thickness function of A (1/fm^2)'
      write(*,*)'TB ................ thickness function of B (1/fm^2)'
      write(*,*)'TAB ............... overlap function of A+B (1/fm^2)'
      write(*,*)'TABcheck........... TAB calculated via TA and TB'
      write(*,*)'Apart ............. number of participants from A'
      write(*,*)'Bpart ............. number of participants from B'
      write(*,*)'sigma ............. cross section ds/db*0.1 fm (fm^2)'
      write(*,*)'cent .............. normalized integral cross section'
      write(*,900)

c Print data
c-----------
      write(*,901)'b','nA','nB','TA','TB','TAB','TABcheck', 
     +            'Apart', 'Bpart','sigma','cent'
      do i=1,200
        write(*,905)b(i),density(A1,0.0d0,0.0d0,b(i)),
     +              density(A2,0.0d0,0.0d0,b(i)),
     +              TA1(i),TA2(i),TA1A2(i),TA1A2check(i),
     +              npart1(i),npart2(i),
     +              sigma(i),sigmasum(i)/sigmasum(200)
      enddo
      stop

 900  format('************************************************',
     +       '************************************************')
 901  format(a6,4a8,4a10,a8,a10)
 905  format(f6.2,4f8.3,4f10.3,f8.3,f10.5)
 908  format(1x,a,f6.3,1x,a)
      end
*******************************************************************************
c iflag=1 - sharp sphere
c iflag=2 - Woods-Saxon
      double precision function density(A,x,y,z)
      implicit none
      double precision A,x,y,z
      double precision density0/0.17/
      double precision RA,dr,r
      integer denflag
      common denflag

      r=sqrt(x*x+y*y+z*z)      

      if (denflag.eq.1) then 
        RA=(A/4.0*3.0/3.1415/density0)**0.3333333
        density=0.0
        if (r.le.RA) density=density0
      elseif (denflag.eq.2) then 
        RA=1.12*A**0.333333-0.86/A**0.333333

c       RA=1.19*A**0.333333-1.61/A**0.333333
c       density0=3./4.*A/3.1416/RA**3/(1+3.1416**2*0.54**2/RA**2)

        DR=0.54
        density=density0/(1+exp((r-RA)/dr))
      else 
        write(*,*)'wrong density profile flag'
        stop
      endif
      return
      end
*******************************************************************************
      double precision function TA(A,b)
      implicit none
      double precision A,b
      double precision z,density
      double precision rmax
      integer denflag,nshot
      common denflag,nshot,rmax
      real rand
      integer j

      TA=0.0
      do j=1,nshot
        z=rand()*rmax
        TA=TA+density(A,b,0.0d0,z)
      enddo
      ta=TA/nshot*2*rmax
      return
      end
*******************************************************************************
c direct calculation of TAB (not via TA*TB)
      double precision function TAB(A1,A2,b)
      implicit none
      double precision density
      double precision A1,A2,x,y,za,zb
      double precision b,o
      real rand
      integer j
      double precision rmax
      integer denflag,nshot
      common denflag,nshot,rmax

      TAB=0.0
      do j=1,nshot
        x=(rand()-0.5)*2*rmax
        y=(rand()-0.5)*2*rmax
        za=(rand()-0.5)*2*rmax
        zb=(rand()-0.5)*2*rmax
        o=density(A1,x+b,y,za)*density(A2,x,y,zb)
        TAB=TAB+o
      enddo
      TAB=TAB/nshot*(2*rmax)**4
      return
      end
*******************************************************************************
c TAB and npart calculation via TA and TB
c npart1 and npart2 are the respective numbers of participants from A1 and A2
c sigma_NN is in millibarn and TA1 and TA2 are in fm^-2 
c sigma_NN*TA/10 is mean number of NN collisions.
c Vector b points from A to B.

      subroutine NPART(A1,A2,b,sigma_NN,TA1,TA2,TA1A2,npart1,npart2)
      implicit none
      double precision A1,A2,b,sigma_NN,TA1A2,npart1,npart2
      double precision TA1(200),TA2(200)
      double precision rmax
      integer denflag,nshot
      common denflag,nshot,rmax
      real rand
      double precision x,y,b1,b2
      integer ib1,ib2
      integer j

      TA1A2 =0.0
      npart1=0.0
      npart2=0.0
      do j=1,nshot
        x=(rand()-0.5)*2*rmax
        y=(rand()-0.5)*2*rmax
        b1=sqrt(x**2+y**2)
        b2=sqrt((x-b)**2+y**2)
        ib1=int(b1*10+1.0)
        ib2=int(b2*10+1.0)
        ib1=min(ib1,200)
        ib2=min(ib2,200)
        TA1A2=TA1A2+TA1(ib1)*TA2(ib2)
        npart1=npart1+TA1(ib1)*(1-exp(-sigma_NN*TA2(ib2)/10))
        npart2=npart2+TA2(ib2)*(1-exp(-sigma_NN*TA1(ib1)/10))
c       npart1=npart1+TA1(ib1)*(1-(1-sigma_NN*TA2(ib2)/10/A2)**A2)
c       npart2=npart2+TA2(ib2)*(1-(1-sigma_NN*TA1(ib1)/10/A1)**A1)
      enddo
      TA1A2=TA1A2/nshot*(2*rmax)**2
      npart1=npart1/nshot*(2*rmax)**2
      npart2=npart2/nshot*(2*rmax)**2
      return
      end
*******************************************************************************
