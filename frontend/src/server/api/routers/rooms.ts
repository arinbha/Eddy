import { z } from "zod";

import {
  createTRPCRouter,
  protectedProcedure,
  publicProcedure,
} from "~/server/api/trpc";

export const roomsRouter = createTRPCRouter({
  search: publicProcedure.query(async ({ ctx }) => {
    // const { data } = await ctx.client.get("https://localhost:8080/search");
    const data = ["GHC Commons 6", "Next Study Space", "Hunt Libarary Studio A"]

    const schema = z.string().array();

    const result = await schema.safeParseAsync(data);

    if (result.success) 
      return result.data;
  }),
});
