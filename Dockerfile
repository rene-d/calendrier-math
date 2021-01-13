FROM debian

RUN apt-get -qq update \
&&  apt-get -qq install -y git ruby ruby-dev build-essential zlib1g-dev

RUN git clone https://github.com/pages-themes/tactile \
&&  cd tactile \
&&  script/bootstrap

RUN gem install github-pages

CMD bundle exec jekyll serve -H 0.0.0.0 -s /site
