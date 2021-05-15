<template>
  <div class="mt-3">
    <h5 class="text-uppercase">
      <i class="mdi mdi-briefcase mr-1"></i>
      Experience
    </h5>

    <div class="timeline-alt pb-0">
      <div class="timeline-item">
        <i class="mdi mdi-circle bg-info-lighten text-info timeline-icon"></i>
        <div class="timeline-item-info">
          <h5 class="mt-0 mb-1">Lead designer / Developer</h5>
          <p class="font-14">
            websitename.com
            <span class="ml-2 font-12">Year: 2015 - 18</span>
          </p>
          <p class="text-muted mt-2 mb-0 pb-3">
            Everyone realizes why a new common language
            would be desirable: one could refuse to pay expensive translators.
            To achieve this, it would be necessary to have uniform grammar,
            pronunciation and more common words.
          </p>
        </div>
      </div>

      <div class="timeline-item">
        <i class="mdi mdi-circle bg-primary-lighten text-primary timeline-icon"></i>
        <div class="timeline-item-info">
          <h5 class="mt-0 mb-1">Senior Graphic Designer</h5>
          <p class="font-14">
            Software Inc.
            <span class="ml-2 font-12">Year: 2012 - 15</span>
          </p>
          <p class="text-muted mt-2 mb-0 pb-3">
            If several languages coalesce, the grammar
            of the resulting language is more simple and regular than that of
            the individual languages. The new common language will be more
            simple and regular than the existing European languages.
          </p>
        </div>
      </div>

      <div class="timeline-item">
        <i class="mdi mdi-circle bg-info-lighten text-info timeline-icon"></i>
        <div class="timeline-item-info">
          <h5 class="mt-0 mb-1">Graphic Designer</h5>
          <p class="font-14">
            Coderthemes Design LLP
            <span class="ml-2 font-12">Year: 2010 - 12</span>
          </p>
          <p class="text-muted mt-2 mb-0 pb-2">
            The European languages are members of
            the same family. Their separate existence is a myth. For science
            music sport etc, Europe uses the same vocabulary. The languages
            only differ in their grammar their pronunciation.
          </p>
        </div>
      </div>
    </div>
    <!-- end timeline -->

    <h5 class="mb-3 mt-4 text-uppercase">
      <i class="mdi mdi-cards-variant mr-1"></i>
      Projects
    </h5>
    <b-table-simple borderless responsive class="table-nowrap mb-0">
      <b-thead class="thead-light">
        <b-tr>
          <b-th>#</b-th>
          <b-th>Clients</b-th>
          <b-th>Project Name</b-th>
          <b-th>Start Date</b-th>
          <b-th>Due Date</b-th>
          <b-th>Status</b-th>
        </b-tr>
      </b-thead>
      <b-tbody>
        <b-tr>
          <b-td>1</b-td>
          <b-td>
            <img
              src="@assets/images/users/avatar-2.jpg"
              alt="table-user"
              class="mr-2 rounded-circle"
              height="24"
            /> Halette Boivin
          </b-td>
          <b-td>App design and development</b-td>
          <b-td>01/01/2015</b-td>
          <b-td>10/15/2018</b-td>
          <b-td>
            <span class="badge badge-info-lighten">Work in Progress</span>
          </b-td>
        </b-tr>
        <b-tr>
          <b-td>2</b-td>
          <b-td>
            <img
              src="@assets/images/users/avatar-3.jpg"
              alt="table-user"
              class="mr-2 rounded-circle"
              height="24"
            /> Durandana Jolicoeur
          </b-td>
          <b-td>Coffee detail page - Main Page</b-td>
          <b-td>21/07/2016</b-td>
          <b-td>12/05/2018</b-td>
          <b-td>
            <span class="badge badge-danger-lighten">Pending</span>
          </b-td>
        </b-tr>
        <b-tr>
          <b-td>3</b-td>
          <b-td>
            <img
              src="@assets/images/users/avatar-4.jpg"
              alt="table-user"
              class="mr-2 rounded-circle"
              height="24"
            /> Lucas Sabourin
          </b-td>
          <b-td>Poster illustation design</b-td>
          <b-td>18/03/2018</b-td>
          <b-td>28/09/2018</b-td>
          <b-td>
            <span class="badge badge-success-lighten">Done</span>
          </b-td>
        </b-tr>
        <b-tr>
          <b-td>4</b-td>
          <b-td>
            <img
              src="@assets/images/users/avatar-6.jpg"
              alt="table-user"
              class="mr-2 rounded-circle"
              height="24"
            /> Donatien Brunelle
          </b-td>
          <b-td>Drinking bottle graphics</b-td>
          <b-td>02/10/2017</b-td>
          <b-td>07/05/2018</b-td>
          <b-td>
            <span class="badge badge-info-lighten">Work in Progress</span>
          </b-td>
        </b-tr>
        <b-tr>
          <b-td>5</b-td>
          <b-td>
            <img
              src="@assets/images/users/avatar-5.jpg"
              alt="table-user"
              class="mr-2 rounded-circle"
              height="24"
            /> Karel Auberjo
          </b-td>
          <b-td>Landing page design - Home</b-td>
          <b-td>17/01/2017</b-td>
          <b-td>25/05/2021</b-td>
          <b-td>
            <span class="badge badge-warning-lighten">Coming soon</span>
          </b-td>
        </b-tr>
      </b-tbody>
    </b-table-simple>
  </div>
</template>