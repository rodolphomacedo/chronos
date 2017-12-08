# **Chronos**
## Finding an optimal way to assign nurses to shifts

![Scheduling Nurse](static/nurse_clock_date.png)

It is required to schedule monthly the nurses'shifts. A working shift or a day off must 
be assigned to each nurse in each day of the month. In each day there are three working shifts:

    * Morning shift
    * Afternoon shift
    * Night shift

According to the ward policy, nurses may require to have a rest on a particular day: this type 
of rest is referred to as requested day off.
Further, they may also ask not to be assigned to a specific working shift in a given day of the week,
*e.g.* a nurse may ask not to be assigned to a night shift on Friday.
This second type of request is referred to as things that are desired, henceforth *desiderata*.
The monthly schedule must also satisfy several contractual and operational requirements.


### The main contractual requirements are:
    1. The number of days off per month must be equal to a predefined value provided by the ward management.
    2. The nurses requirements related to holidays and requested days off must be satisfied.
    3. A nurse cannot work consecutively for more than K days.
    4. The night shifts must be allocated in sets of minimum L and maximum M consecutive days.
    5. After a set of night shifts, there must be at least N days off.
    6. An interval of at least P days must occur between two night shifts sets.

In the above requirements, K, L, M, N and P are parameters chosen by the ward management.


### The main operational requirements are:
    1. A minimum number of nurses must be guaranteed for each working shift. This parameter, provided
    by the ward management, may differ from shift to shift and from day to day.
    2. A nurse assigned to an afternoon shift in a given day must not be assigned to a morning shift in the
    following day.
    3. A balanced assignment of morning, afternoon and night working shifts must be guaranteed among
    the nurses.
    4. Working shifts and days off during the week-ends must be evenly assigned.
    5. The so-called nurses'*desiderata* should be satisfied as much as possible.

The ward management provided also the following optional advices to be possibly respected:

    1. Try to assign a set of morning shifts before the first day of a holidays period and a set of night shifts
    after a holidays period.
    2. Try to assign two days off after K consecutive working days.
    3. Try to avoid the assignment of a night shift before a requested day off.
    4. Try to allocate night shifts in sets of M-1 days, avoiding however the end of the set on Saturday by adding, when
    necessary, one more night shift.
    5. Try to allocate day shifts in set of three consecutive days. 
