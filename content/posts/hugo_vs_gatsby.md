+++
title = "Hugo vs Gatsby"
date = 2020-07-04T16:37:44-05:00
draft = false
summary = "A breakdown of what I've learned testing out Gatsby and why I moved back to Hugo for my site."
tags = ["hugo", "spa", "gatsby"]
categories = ["development"]
type = "posts"
+++
For the longest time I've wanted to build a proper website using all the fun JavaScript and CSS tricks that full-stack devs do (and that I've been jealous of). As a platform / systems / operations engineer, my speciality is in using code to build systems. Front-end design, UI and UX, accessibility, and so many more things are just not part of my day-to-day activities. I think tha they are all incredibly valuable, but my career is hard enough to keep up with technological changes happening in my own tech field, much less those happening in fields that are far outside of my speciality. So I gave it a shot and tried out [Gatsby](gatsbyjs.org/) when I started to redesign this site.

## What is Gatsby?
[Gatsby](gatsbyjs.org/) is a React-based web framework that uses [GraphQL](https://graphql.org/) to render content from a variety of sources. The advantages are many. Using various plug-ins you can pull content from many types of data sources, including S3 and WordPress. Plug-ins can also help you render data in different formats, like Markdown or JSON. The philosophy of the framework emphasises reusability and components. This makes designing flexible layouts and page components easy to do. Top this off with the ability to generate a static site that you can host pretty much everywhere and you can see why it's so exciting.

To my non-developer brain, it feels something like functional programming for the web. Put another 
way, [Gatsby](gatsbyjs.org/) is to static site generators as 
[Troposphere](https://github.com/cloudtools/troposphere) is to 
[CloudFormation](https://aws.amazon.com/cloudformation/). Gatsby can render different content types 
from different sources, from S3 to other content management systems. This is all fused together 
and rendered as web content in a holistic fashion. Another interesting aspect to Gatsby is it 
leverages a GraphQL data model to drive all the different plugins and processors. There's even a 
built-in GraphQL workbench you can access to query content and play around with. 
Lastly, [Gatsby Tutorial](https://www.gatsbyjs.org/tutorial/) is very well thought out and provides a 
gentle ramp for inexperienced developers. 

## Why I Stuck with Hugo
The reason boils down to choosing the right tool for my needs. At the end of the day I'm writing a 
blog with some static content. Hugo already does this quite well and the ecosystem is constantly 
growing. If I were making a true webapp or building something more complex, I would absolutely choose 
to go with Gatsby. I have a side project I'm working on right now and it may be a perfect fit. But 
for this site, and for what I'm doing here, Hugo is still the best choice.